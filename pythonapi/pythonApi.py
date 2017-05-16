import requests
class PythonApi:

    def __init__(self, user, password, base_url, site, version):
        self._user = user
        self._password = password
        self._base_url = base_url
        self._site = site
        self._version = version
        self._is_logged_in = False

        self._cookies = '';

    def __del__(self):
        if self._is_logged_in:
            self._log_out()

    def _log_in(self):
        self._cookies = ''

        headers = { 'referer': self._base_url + '/login' }
        url = self._base_url + '/api/login'

        response = requests.post(url, headers=headers)
        self._cookies = response.cookies[0]
        self._is_logged_in = True
        return True


    def _log_out(self):
        if self._is_logged_in:
            return False
        response = requests.get(self._base_url + '/logout')
        self._is_logged_in = False
        self._cookies = ''
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