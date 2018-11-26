DEFAULT_LIC_DIR="/serverspeeder/etc/"

lic_file=`ls ${DEFAULT_LIC_DIR} | grep lic$`
lic_path="${DEFAULT_LIC_DIR}/${lic_file}"
cp "${lic_path}" "${lic_path}".bak

echo "Validating your license ..."
echo 
echo "Please enter your key :"
read key
t=`xxd ${lic_path} | sed "/0000040/c\0000040: ${key}"`
xxd -r > ${lic_path} <<< "$t"


# diff <(xxd "${lic_path}") <("${lic_path}".bak)


# cat >val_lic.sh <<-'eof'
# DEFAULT_LIC_DIR="/serverspeeder/etc/"
# 
# lic_file=`ls ${DEFAULT_LIC_DIR} | grep lic$`
# lic_path="${DEFAULT_LIC_DIR}/${lic_file}"
# cp "${lic_path}" "${lic_path}".bak
# 
# echo "Validating your license ..."
# echo 
# echo "Please enter your key :"
# read key
# t=`xxd ${lic_path} | sed "/0000040/c\0000040: ${key}"`
# xxd -r > ${lic_path} <<< "$t"
# eof
