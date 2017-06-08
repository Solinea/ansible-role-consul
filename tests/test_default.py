import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_consul_running_and_enabled(host):
    consul = host.service("consul")
    assert consul.is_running
    assert consul.is_enabled
