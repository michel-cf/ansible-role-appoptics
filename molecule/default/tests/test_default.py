import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_appoptics_directory(host):
    d = host.file('/opt/SolarWinds/Snap/')

    assert d.exists
    assert d.user == 'solarwinds'
    assert d.group == 'solarwinds'


def test_appoptics_config(host):
    d = host.file('/opt/SolarWinds/Snap/etc/config.yaml')

    assert d.exists
    assert d.user == 'solarwinds'
    assert d.group == 'solarwinds'


def test_appoptics_service(host):
    s = host.service('swisnapd')

    assert s.is_running
