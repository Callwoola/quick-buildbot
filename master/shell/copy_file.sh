#!/usr/bin/env bash


#workdir  -> /opt/dmc/server
#workdir  -> /opt/dmc/webapp


sudo mkdir -p /opt/dmc/dmc_engine
sudo cp -rf /root/slave/dmc/_root_storage_dmc/build/engine /opt/dmc/
echo  '>>>>>>>>>>>>>>>>>>>>>>>>>>>>> copy done!'


sudo mkdir -p /opt/dmc/dmc_webapp
sudo cp -rf /root/slave/dmc/_root_storage_dmc/build/webapp /opt/dmc/
echo  '>>>>>>>>>>>>>>>>>>>>>>>>>>>>> copy done!'
