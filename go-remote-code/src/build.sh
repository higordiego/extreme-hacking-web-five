``bash
#!/usr/bin/env bash
set -e
echo "[+] Building <Go Remote Code>"
echo "[+] OS: Debian 12"
echo "[+] Author: <Higor Diego>"
echo "[+] Date: 11/04/2024"
echo "[+] Dificuldade: Difícil"

apt update -y
apt upgrade -y

echo "[+] OS atualizado"

apt-get -y install ca-certificates curl gnupg
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
chmod a+r /etc/apt/keyrings/docker.gpg

echo "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian"$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
apt-get -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin


echo "[+] Pacotes necessários"
cd /root
docker build -t go-remote-code . --no-cache
docker run -d --restart=always -p8000:5000 -e PORT="5000" --hostname go-remote-code --name go-remote-code go-remote-code


echo "[+] Disabling IPv6"
echo "net.ipv6.conf.all.disable_ipv6 = 1" >> /etc/sysctl.conf
echo "net.ipv6.conf.default.disable_ipv6 = 1" >> /etc/sysctl.conf
sed -i 's/GRUB_CMDLINE_LINUX_DEFAULT=""/GRUB_CMDLINE_LINUX_DEFAULT="ipv6.disable=1"/' /etc/default/grub
sed -i 's/GRUB_CMDLINE_LINUX=""/GRUB_CMDLINE_LINUX="ipv6.disable=1"/' /etc/default/grub
update-grub

echo "[+] Setting passwords"
echo "root:SENHA_INQUEBRAVEL" | chpasswd

echo "[+] Cleaning up"
ln -sf /dev/null /root/.bash_history
userdel -r lab
apt clean -y
apt autoremove -y
rm -rf /root/*

for user in $(ls /home); do
    rm -rf /home/$user/.bash_history
    rm -rf /home/$user/.cache
    rm -rf /home/$user/.viminfo
    rm -rf /home/$user/.sudo_as_admin_successful
    rm -rf /home/$user/.bash_logout
    rm -rf /home/$user/.bashrc
    rm -rf /home/$user/.profile
done

find /var/log -type f -exec sh -c "cat /dev/null > {}" \;

# Clean all tracks
rm -rf /root/.cache
rm -rf /root/.viminfo
rm -rf /root/.sudo_as_admin_successful
rm -rf /root/.bash_logout
rm -rf /root/.bashrc
rm -rf /root/.profile