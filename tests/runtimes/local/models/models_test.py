"""Tests for Models class."""
from ostorlab.runtimes.local.models import models


def testModels_whenDatabaseDoesNotExist_DatabaseAndScanCreated(mocker, db_engine_path):
    """Test when database does not exists, scan is populated in a newly created database."""
    mocker.patch.object(models, 'ENGINE_URL', db_engine_path)
    models.Database().create_db_tables()
    models.Scan.create(title='test', asset='Asset')
    assert models.Database().session.query(models.Scan).count() == 1
    assert models.Database().session.query(models.Scan).all()[0].title == 'test'
    models.Database().drop_db_tables()


def testScanUpdate_always_updatesExistingScan(mocker, db_engine_path):
    """Test Agent save implementation."""
    mocker.patch.object(models, 'ENGINE_URL', db_engine_path)
    models.Database().create_db_tables()
    models.Scan.create('test')

    database = models.Database()
    database.session.commit()
    assert database.session.query(models.Scan).count() == 1
    scan = database.session.query(models.Scan).first()
    scan.title = 'test2'
    database.session.commit()

    assert database.session.query(models.Scan).count() == 1
    scan = database.session.query(models.Scan).first()
    assert scan.title == 'test2'


def testModelsVulnerability_whenDatabaseDoesNotExist_DatabaseAndScanCreated(mocker, db_engine_path):
    """Test Vulnerability Model implementation."""
    mocker.patch.object(models, 'ENGINE_URL', db_engine_path)
    models.Database().create_db_tables()
    create_scan_db = models.Scan.create('test')
    init_count = models.Database().session.query(models.Vulnerability).count()
    models.Vulnerability.create(title='MyVuln', short_description='Xss', description='Javascript Vuln',
                                recommendation='Sanitize data', technical_detail='a=$input', risk_rating='HIGH',
                                cvss_v3_vector='5:6:7', dna='121312',
                                location={
                                    'ios_store': {'bundle_id': 'some.dummy.bundle'},
                                    'metadata': [
                                        {'type': 'CODE_LOCATION', 'value': 'some/file.swift:42'}
                                    ]
                                },
                                scan_id=create_scan_db.id)

    assert models.Database().session.query(models.Vulnerability).count() == init_count + 1
    assert models.Database().session.query(models.Vulnerability).all()[0].title == 'MyVuln'
    assert models.Database().session.query(models.Vulnerability).all()[0].scan_id == create_scan_db.id
    assert 'iOS bundle ID: some.dummy.bundle' in models.Database().session.query(models.Vulnerability).all()[0].location


def testModelsScanStatus_whenDatabaseDoesNotExist_DatabaseAndScanCreated(mocker, tmpdir, db_engine_path):
    """Test Scan Status Model implementation."""
    mocker.patch.object(models, 'ENGINE_URL', db_engine_path)
    models.Database().create_db_tables()
    create_scan_db = models.Scan.create('test')
    init_count = models.Database().session.query(models.ScanStatus).count()
    models.ScanStatus.create(key='status', value='in_progress', scan_id=create_scan_db.id)

    assert models.Database().session.query(models.ScanStatus).count() == init_count + 1
    assert models.Database().session.query(models.ScanStatus).all()[-1].key == 'status'
    assert models.Database().session.query(models.ScanStatus).all()[-1].value == 'in_progress'
    assert models.Database().session.query(models.ScanStatus).all()[-1].scan_id == create_scan_db.id
