import requests
class PythonApi:

    def __init__(self, user=None, password=None, base_url=None, site=None, version=None):
        self.user = ''
        self.password = ''
        self.site = 'default'
        self.base_url = 'https://127.0.0.1:8443'
        self.version = '4.8.20'
        self.is_logged_in = False
        self.debug = False

        if user:
            self.user = user
        if password:
            self.password = password
        if base_url:
            self.base_url = base_url
        if site:
            self.site = site
        if version:
            self.version = version

        self.session = None

    def __del__(self):
        if self.is_logged_in:
            self.logout()

    def login(self):
        if self.session:
            self.session.close()
            self.session = None

        self.session = requests.session()
        headers = {'referer': self.base_url + '/login'}
        url = self.base_url + '/api/login'

        login_info = {'username': self.user, 'password': self.password}

        response = self.session.post(url, headers=headers, json=login_info)

        if self.debug:
            print(response.text)

        try:
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return False

        self.is_logged_in = True
        return True

    def logout(self):
        if self._is_logged_in:
            return False
        response = self.session.get(self._base_url + '/logout')

        try:
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return False

        self.is_logged_in = False
        self.session.close()

        return True

    def authorize_guest(self, mac, minutes, up=None, down=None, m_bytes=None, ap_mac=None):
        raise NotImplementedError

    def unauthorize_guest(self, mac):
        raise NotImplementedError

    def reconnect_sta(self, mac):
        raise NotImplementedError

    def block_sta(self, mac):
        raise NotImplementedError

    def unblock_sta(self, mac):
        raise NotImplementedError

    def set_sta_note(self, user_id, note=None):
        raise NotImplementedError

    def set_sta_name(self, user_id, name=None):
        raise NotImplementedError

    def stat_daily_site(self, start=None, end=None):
        raise NotImplementedError

    def stat_hourly_site(self, start=None, end=None):
        raise NotImplementedError

    def stat_hourly_aps(self, start=None, end=None):
        raise NotImplementedError

    def stat_daily_aps(self, start=None, end=None):
        raise NotImplementedError

    def stat_sessions(self, start=None, end=None, mac=None):
        raise NotImplementedError

    def stat_sta_sessions_latest(self, mac, limit=None):
        raise NotImplementedError

    def stat_auths(self, start=None, end=None):
        raise NotImplementedError

    def stat_allusers(self, history_hours=8760):
        raise NotImplementedError

    def list_guests(self, within=8760):
        raise NotImplementedError

    def list_clients(self, client_mac=None):
        raise NotImplementedError

    def stat_client(self, client_mac):
        raise NotImplementedError

    def list_usergroups(self):
        raise NotImplementedError

    def set_usergroup(self, user_id, group_id):
        raise NotImplementedError

    def list_health(self):
        raise NotImplementedError

    def list_dashboard(self):
        raise NotImplementedError

    def list_users(self):
        raise NotImplementedError

    def list_aps(self, device_mac=None):
        raise NotImplementedError

    def list_rogueaps(self, within='24'):
        raise NotImplementedError

    def list_sites(self):
        raise NotImplementedError

    def stat_sites(self):
        raise NotImplementedError

    def add_site(self, description):
        raise NotImplementedError

    def delete_site(self, site_id):
        raise NotImplementedError

    def list_admins(self):
        raise NotImplementedError

    def list_wlan_groups(self):
        raise NotImplementedError

    def stat_sysinfo(self):
        raise NotImplementedError

    def list_self(self):
        raise NotImplementedError

    def list_networkconf(self):
        raise  NotImplementedError

    def stat_voucher(self, create_time=None):
        raise NotImplementedError

    def stat_payment(self, within=None):
        raise NotImplementedError

    def create_hotspotop(self, name, x_password, note=None):
        raise NotImplementedError

    def list_hotspotop(self):
        raise NotImplementedError

    def create_voucher(self, minutes, count=1, quota='0', note=None, up=None, down=None, m_bytes=None):
        raise NotImplementedError

    def revoke_voucher(self, voucher_id):
        raise NotImplementedError

    def extend_guest_validity(self, guest_id):
        raise NotImplementedError

    def list_portforward_stats(self):
        raise NotImplementedError

    def list_portforwarding(self):
        raise NotImplementedError

    def list_dynamicdns(self):
        raise  NotImplementedError

    def list_extension(self):
        raise  NotImplementedError

    def list_settings(self):
        raise NotImplementedError

    def adopt_device(self, mac):
        raise NotImplementedError

    def restart_ap(self, mac):
        raise NotImplementedError

    def disable_ap(self, ap_id, disable):
        raise NotImplementedError

    def led_override(self, device_id, override_mode):
        raise NotImplementedError

    def set_locate_ap(self, mac):
        raise NotImplementedError

    def unset_locate_ap(self, mac):
        raise NotImplementedError

    def site_ledson(self):
        raise NotImplementedError

    def site_ledsoff(self):
        raise NotImplementedError

    def set_ap_radiosettings(self, ap_id, radio, channel, ht, tx_power_mode, tx_power):
        raise NotImplementedError

    def set_guest_login_settings(self, portal_enabled, portal_customized, redirect_enabled, redirect_url, x_password, expire_number, expire_unit, site_id):
        raise NotImplementedError

    def rename_ap(self, ap_id, ap_name):
        raise NotImplementedError

    def create_wlan(self, name, x_passphrase, user_group_id, wlan_group_id, enabled=None, hide_ssid=None, is_guest=None, security=None, wpa_mode=None, wpa_enc=None, vlan_enabled=None, vlan=None, uapsd_enabled=None, schedule_enabled=None, schedule=None):
        raise NotImplementedError

    def delete_wlan(self, wlan_id):
        raise NotImplementedError

    def set_wlan_settings(self, wlan_id, x_passphrase, name=None):
        raise NotImplementedError

    def disable_wlan(self, wlan_id, disable):
        raise NotImplementedError

    def list_events(self):
        raise NotImplementedError

    def list_wlan_conf(self):
        raise NotImplementedError

    def list_alarms(self):
        raise NotImplementedError