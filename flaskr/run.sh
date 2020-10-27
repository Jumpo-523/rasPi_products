sed -e 's/:[^:\/\/]/="/g;s/$/"/g;s/ *=/=/g' ./config/config.yml | awk '{print "export " $0 }' > set_env.sh



# echo 'echo "動作確認" \necho $LINE_CHANNEL_ACCESS_TOKEN' >> set_env.sh

source set_env.sh


flask run

rm set_env.sh

