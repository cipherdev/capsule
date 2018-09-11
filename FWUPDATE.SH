#!/bin/bash

if [ -f /etc/os-release ]; then
	echo "Install the tools to development on CentOS"
	yum groupinstall -y "Development Tools"
	yum install -y gcc make wget elfutils* gnu-efi* popt*
	echo "Install efivar and fwupdate"
	rpm -ivh --force *.rpm
elif [ -f /etc/oracle ]; then
	echo "Install the tools to development"
	yum groupinstall -y "Development Tools"
	yum install -y gcc make wget
	#Add repository
cat << EOF >> /etc/yum.repos.d/public-yum-ol7.repo
	[tools_repo]
	name=Tools need to install gnu-efi elfutils popt ($basearch)
	baseurl=http://yum.oracle.com/repo/OracleLinux/OL7/latest/aarch64
	enabled=1
	gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-oracle
	gpgcheck=0
EOF
	# Install the package from repo
	yum install -y gnu-efi* elfutils* popt* libfwup*
	echo "Install efivar and fwupdate"
	rpm -ivh --force *.rpm
elif [ -f /etc/ubuntu ]; then
	echo "ubuntu doesn't support"
fi
