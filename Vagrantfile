#Requirements - version of Vagrant
Vagrant.require_version ">= 1.8.0"

Vagrant.configure("2") do |config|
    config.vm.box = "bento/ubuntu-20.04"

    #Configuration of VM
    config.vm.provider :virtualbox do |v|
        v.gui = false
        v.memory = 2048

    #Ansible - provision
    config.vm.provision "ansible" do |ansible|
        ansible.verbose = "v"
        ansible.playbook = "playbook.yml"
  end
end