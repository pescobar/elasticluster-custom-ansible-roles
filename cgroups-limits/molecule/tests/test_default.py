import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_cgroup_is_installed(host):
    assert host.package("libcgroup").is_installed
    assert host.package("libcgroup-tools").is_installed


def test_cgroup_conf_file(host):
    f = host.file("/etc/cgconfig.conf")
    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0644'
    assert f.contains("memory.limit_in_bytes")

    f2 = host.file("/etc/cgrules.conf")
    assert f2.exists
    assert f2.is_file
    assert f2.user == 'root'
    assert f2.group == 'root'
    assert oct(f2.mode) == '0644'
    assert f.contains("memory")


def test_cgroup_services(host):
    assert host.service('cgconfig').is_running
    assert host.service('cgred').is_running
