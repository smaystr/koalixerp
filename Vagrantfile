Vagrant.configure('2') do |config|

    config.vm.provider "virtualbox"
    config.vm.box = 'ubuntu/trusty64'
    # This line is needed to construc the initial provision because the lxml
    # Python library needs 1GB of RAM to compile, but the Vagrant starting
    # process will not validate the command after that.
    
    # config.vm.customize ["modifyvm", :id, "--memory", 1024]
    config.vm.provision "shell", path: "provision.sh"

    config.ssh.forward_agent = true
    # Forward the dev server port
    config.vm.network :forwarded_port, host: 9000, guest: 8000
    config.vm.network :forwarded_port, host: 5434, guest: 5432
end
