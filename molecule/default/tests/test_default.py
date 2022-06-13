import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_geth_running_and_enabled(host):
    geth = host.service('geth')

    assert geth.is_enabled

# def test_port_is_listening(host):
#     socket = host.socket("tcp://localhost:8545")
#     assert(socket.is_listening)

def test_port(host):
    command = "curl --digest -L -D - http://localhost:8545"

    cmd = host.run(command)
    assert 'HTTP/1.1 200 OK' in cmd.stdout