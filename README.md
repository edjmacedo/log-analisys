# log analisys
Log analisys consist answer three questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Pre requisites ##

You will need:
- Python >= 2.76
- Virtual Box with Vagrand configured

* Optionally, should be running in local machine, without virtual machine.

## Virtual Box and Vagrant ##

- Download and install Virtual Box: [Virtual Box](https://www.virtualbox.org/)
- Download and install Vagrant: [Vagrant](https://www.vagrantup.com/downloads.html)

## Configuring Vagrant ##

- Download this virtual Machine: [Base Virtual Machine](https://d17h27t6h515a5.cloudfront.net/topher/2017/April/58fe3483_fsnd-virtual-machine/fsnd-virtual-machine.zip)
- Unzip and go to directory and running with: `vagrant up`
- after that, run: `vagrant ssh`

## Running swiss tournament ##

- Clone log analisys repository
- Paste in vagrant folder
- Inside log project, unzip newsdata.sql
- up Vagrant: `vagrant up`
- Log in vagrant: `vagrant ssh`
- Go to vagrant directory: `cd /vagrant/`
- run psql: `psql`
- load the data, use the command `psql -d news -f newsdata.sql`
- select news as main database: `\c news`
- run log questions: `python log.py`
