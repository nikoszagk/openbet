Vagrant.require_version ">= 1.7.0"

Vagrant.configure("2") do |config|

    config.vm.box = "bento/ubuntu-20.04"
    config.ssh.insert_key = false
    config.vm.define "openbet" do |openbet|
        openbet.vm.hostname = "openbet"
        openbet.vm.provider :virtualbox do |vb|
            vb.name = "openbetDevOps"
        end
    end
    config.vm.provision "ansible" do |ansible|
        ansible.verbose = "v"
        ansible.playbook = "playbook.yml"
        ansible.become = true
   end
end