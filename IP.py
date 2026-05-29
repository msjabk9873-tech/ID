#!/usr/bin/env python3
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   ★ IP UNBLOCK TOOL v3.0 - Android Edition ★
#   Developer: فيصل سعيدي
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
import subprocess
import requests
import random
import time
import sys
import os
import json
import socket
import threading
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# ═══════════════════════════════════════════
#               COLORS & UI (تم التعديل)
# ═══════════════════════════════════════════
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    BG_GREEN = '\033[42m'
    BG_RED = '\033[41m'
    BG_BLUE = '\033[44m'
    # ألوان جديدة مخصصة
    ORANGE = '\033[38;5;208m'
    PURPLE = '\033[38;5;129m'
    PINK = '\033[38;5;206m'
    GOLD = '\033[38;5;220m'
    DARK_RED = '\033[38;5;124m'
    BG_BLACK = '\033[40m'

C = Colors

def clear():
    os.system('clear')

def banner():
    clear()
    print(f"""{C.PURPLE}{C.BOLD}
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │      ██╗██████╗     ██╗   ██╗███╗   ██╗██████╗ ██╗      ██████╗  │
    │      ██║██╔══██╗    ██║   ██║████╗  ██║██╔══██╗██║     ██╔═══██╗ │
    │      ██║██████╔╝    ██║   ██║██╔██╗ ██║██████╔╝██║     ██║   ██║ │
    │      ██║██╔═══╝     ██║   ██║██║╚██╗██║██╔══██╗██║     ██║   ██║ │
    │      ██║██║         ╚██████╔╝██║ ╚████║██████╔╝███████╗╚██████╔╝ │
    │      ╚═╝╚═╝          ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝ ╚═════╝  │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
    {C.RESET}
    {C.GOLD}{'☠' * 62}{C.RESET}
    {C.ORANGE}{C.BOLD}        ███████╗██╗███████╗ █████╗ ██╗         ███████╗ █████╗ ███████╗██╗██████╗ ██╗
    {C.ORANGE}{C.BOLD}        ██╔════╝██║██╔════╝██╔══██╗██║         ██╔════╝██╔══██╗██╔════╝██║██╔══██╗██║
    {C.ORANGE}{C.BOLD}        ███████╗██║█████╗  ███████║██║         ███████╗███████║█████╗  ██║██║  ██║██║
    {C.ORANGE}{C.BOLD}        ╚════██║██║██╔══╝  ██╔══██║██║         ╚════██║██╔══██║██╔══╝  ██║██║  ██║██║
    {C.ORANGE}{C.BOLD}        ███████║██║██║     ██║  ██║███████╗    ███████║██║  ██║██║     ██║██████╔╝███████╗
    {C.ORANGE}{C.BOLD}        ╚══════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ ╚══════╝
    {C.RESET}
    {C.GOLD}{'☠' * 62}{C.RESET}
    {C.PINK}{C.BOLD}        ★ Advanced IP Unblock Tool v3.0 ★{C.RESET}
    {C.PURPLE}        ◆ Developer: فيصل سعيدي ◆{C.RESET}
    {C.GOLD}{'☠' * 62}{C.RESET}
    """)

def loading_animation(text, duration=2):
    frames = ['☠', '💀', '⚡', '🔥', '🗡️', '🩸']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        print(f'\r  {C.PURPLE}{frames[i % len(frames)]} {C.WHITE}{text}{C.RESET}', end='', flush=True)
        time.sleep(0.1)
        i += 1
    print()

def progress_bar(current, total, prefix='', length=40):
    percent = current / total
    filled = int(length * percent)
    bar = f"{C.GOLD}{'█' * filled}{C.DIM}{'░' * (length - filled)}{C.RESET}"
    print(f'\r  {C.WHITE}{prefix} [{bar}] {C.ORANGE}{percent*100:.1f}%{C.RESET}', end='', flush=True)
    if current == total:
        print()

def print_status(icon, text, color=C.WHITE):
    print(f"  {color}{icon} {text}{C.RESET}")

def print_success(text):
    print_status("✅", text, C.GREEN)

def print_error(text):
    print_status("❌", text, C.RED)

def print_info(text):
    print_status("💀", text, C.PURPLE)

def print_warning(text):
    print_status("⚠️ ", text, C.GOLD)

def print_section(title):
    print(f"\n  {C.GOLD}{'☠' * 55}{C.RESET}")
    print(f"  {C.BOLD}{C.PURPLE}◆ {title}{C.RESET}")
    print(f"  {C.GOLD}{'☠' * 55}{C.RESET}")

# ═══════════════════════════════════════════
#           DNS SERVERS DATABASE
# ═══════════════════════════════════════════
DNS_SERVERS = {
    "Cloudflare": ["1.1.1.1", "1.0.0.1"],
    "Google": ["8.8.8.8", "8.8.4.4"],
    "Quad9": ["9.9.9.9", "149.112.112.112"],
    "OpenDNS": ["208.67.222.222", "208.67.220.220"],
    "AdGuard": ["94.140.14.14", "94.140.15.15"],
    "Comodo": ["8.26.56.26", "8.20.247.20"],
    "CleanBrowsing": ["185.228.168.9", "185.228.169.9"],
    "Verisign": ["64.6.64.6", "64.6.65.6"],
    "DNS.Watch": ["84.200.69.80", "84.200.70.40"],
    "Yandex": ["77.88.8.8", "77.88.8.1"],
}

# ═══════════════════════════════════════════
#         WEBSITES TO TEST
# ═══════════════════════════════════════════
TEST_WEBSITES = [
    {"name": "Google", "url": "https://www.google.com", "icon": "🔍"},
    {"name": "YouTube", "url": "https://www.youtube.com", "icon": "📺"},
    {"name": "Facebook", "url": "https://www.facebook.com", "icon": "📘"},
    {"name": "Twitter/X", "url": "https://www.x.com", "icon": "🐦"},
    {"name": "Instagram", "url": "https://www.instagram.com", "icon": "📷"},
    {"name": "TikTok", "url": "https://www.tiktok.com", "icon": "🎵"},
    {"name": "Reddit", "url": "https://www.reddit.com", "icon": "🤖"},
    {"name": "Amazon", "url": "https://www.amazon.com", "icon": "🛒"},
    {"name": "Wikipedia", "url": "https://www.wikipedia.org", "icon": "📚"},
    {"name": "Netflix", "url": "https://www.netflix.com", "icon": "🎬"},
    {"name": "GitHub", "url": "https://www.github.com", "icon": "💻"},
    {"name": "Telegram", "url": "https://web.telegram.org", "icon": "✈️"},
    {"name": "WhatsApp", "url": "https://web.whatsapp.com", "icon": "💬"},
    {"name": "LinkedIn", "url": "https://www.linkedin.com", "icon": "💼"},
    {"name": "Twitch", "url": "https://www.twitch.tv", "icon": "🎮"},
]

# ═══════════════════════════════════════════
#            CORE FUNCTIONS
# ═══════════════════════════════════════════

class IPUnblockTool:
    def __init__(self):
        self.original_ip = None
        self.new_ip = None
        self.results = []
        self.start_time = None
        self.dns_selected = None
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': self.generate_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
        })

    def generate_user_agent(self):
        """Generate random realistic User-Agent"""
        agents = [
            'Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 13; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 14; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 13; RMX3630) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        ]
        return random.choice(agents)

    def get_current_ip(self):
        """Get current public IP address with details"""
        services = [
            'https://api.ipify.org?format=json',
            'https://ipinfo.io/json',
            'https://api.myip.com',
            'https://ip-api.com/json',
        ]
        for service in services:
            try:
                resp = self.session.get(service, timeout=10)
                data = resp.json()
                ip = data.get('ip') or data.get('query') or data.get('origin')
                if ip:
                    return ip, data
            except:
                continue
        return None, {}

    def get_ip_details(self, ip):
        """Get detailed IP information"""
        try:
            resp = self.session.get(f'http://ip-api.com/json/{ip}?fields=66846719', timeout=10)
            return resp.json()
        except:
            return {}

    def flush_dns_cache(self):
        """Flush DNS cache on Android"""
        commands = [
            'ndc resolver clearnetdns wlan0',
            'ndc resolver flushdefaultif',
            'ip rule flush',
            'ip route flush cache',
            'iptables -F',
            'iptables -t nat -F',
        ]
        success = 0
        for cmd in commands:
            try:
                subprocess.run(cmd.split(), capture_output=True, timeout=5)
                success += 1
            except:
                pass
        return success

    def change_dns(self, dns_name=None):
        """Change DNS settings"""
        if dns_name and dns_name in DNS_SERVERS:
            dns = DNS_SERVERS[dns_name]
        else:
            dns_name = random.choice(list(DNS_SERVERS.keys()))
            dns = DNS_SERVERS[dns_name]

        self.dns_selected = dns_name
        commands = [
            f'setprop net.dns1 {dns[0]}',
            f'setprop net.dns2 {dns[1]}',
            f'setprop net.wlan0.dns1 {dns[0]}',
            f'setprop net.wlan0.dns2 {dns[1]}',
            f'setprop net.rmnet0.dns1 {dns[0]}',
            f'setprop net.rmnet0.dns2 {dns[1]}',
            f'setprop dhcp.wlan0.dns1 {dns[0]}',
            f'setprop dhcp.wlan0.dns2 {dns[1]}',
        ]
        for cmd in commands:
            try:
                subprocess.run(cmd.split(), capture_output=True, timeout=5)
            except:
                pass
        return dns_name, dns

    def generate_mac_address(self):
        """Generate random MAC address"""
        mac = [0x02, random.randint(0x00, 0xff), random.randint(0x00, 0xff),
               random.randint(0x00, 0xff), random.randint(0x00, 0xff), random.randint(0x00, 0xff)]
        return ':'.join(map(lambda x: "%02x" % x, mac))

    def spoof_mac_address(self):
        """Attempt to change MAC address"""
        new_mac = self.generate_mac_address()
        commands = [
            'ip link set wlan0 down',
            f'ip link set wlan0 address {new_mac}',
            'ip link set wlan0 up',
        ]
        for cmd in commands:
            try:
                subprocess.run(cmd.split(), capture_output=True, timeout=5)
            except:
                pass
        return new_mac

    def reset_network_interface(self):
        """Reset network interfaces"""
        commands = [
            'svc wifi disable',
            'sleep 2',
            'svc wifi enable',
            'ip addr flush dev wlan0',
            'dhcpcd wlan0',
        ]
        for cmd in commands:
            try:
                if cmd.startswith('sleep'):
                    time.sleep(int(cmd.split()[1]))
                else:
                    subprocess.run(cmd.split(), capture_output=True, timeout=10)
            except:
                pass

    def toggle_airplane_mode(self):
        """Toggle airplane mode to get new IP"""
        commands_on = [
            'cmd connectivity airplane-mode enable',
            'settings put global airplane_mode_on 1',
            'am broadcast -a android.intent.action.AIRPLANE_MODE --ez state true',
        ]
        commands_off = [
            'cmd connectivity airplane-mode disable',
            'settings put global airplane_mode_on 0',
            'am broadcast -a android.intent.action.AIRPLANE_MODE --ez state false',
        ]

        print_info("☠ تفعيل وضع الطيران...")
        for cmd in commands_on:
            try:
                subprocess.run(cmd.split(), capture_output=True, timeout=5)
            except:
                pass

        time.sleep(3)

        print_info("💀 إلغاء وضع الطيران...")
        for cmd in commands_off:
            try:
                subprocess.run(cmd.split(), capture_output=True, timeout=5)
            except:
                pass

        time.sleep(5)

    def test_website(self, site):
        """Test if a website is accessible"""
        try:
            start = time.time()
            resp = self.session.get(
                site['url'],
                timeout=15,
                allow_redirects=True,
                verify=True
            )
            elapsed = time.time() - start
            return {
                'name': site['name'],
                'icon': site['icon'],
                'url': site['url'],
                'status': resp.status_code,
                'time': round(elapsed * 1000),
                'accessible': resp.status_code < 400,
                'size': len(resp.content),
            }
        except requests.exceptions.Timeout:
            return {
                'name': site['name'],
                'icon': site['icon'],
                'url': site['url'],
                'status': 'TIMEOUT',
                'time': 0,
                'accessible': False,
                'size': 0,
            }
        except Exception as e:
            return {
                'name': site['name'],
                'icon': site['icon'],
                'url': site['url'],
                'status': 'ERROR',
                'time': 0,
                'accessible': False,
                'size': 0,
                'error': str(e)[:50],
            }

    def test_all_websites(self):
        """Test all websites concurrently"""
        results = []
        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = {executor.submit(self.test_website, site): site for site in TEST_WEBSITES}
            done = 0
            for future in as_completed(futures):
                done += 1
                progress_bar(done, len(TEST_WEBSITES), "فحص المواقع")
                result = future.result()
                results.append(result)
        return sorted(results, key=lambda x: x['name'])

    def display_results(self, results):
        """Display test results in a beautiful table"""
        print_section("📊 نتائج الفحص")
        print()

        accessible = sum(1 for r in results if r['accessible'])
        blocked = len(results) - accessible

        # Header
        print(f"  {C.BOLD}{'☠' * 62}{C.RESET}")
        print(f"  {C.BOLD}{C.WHITE} {'الموقع':<20} {'الحالة':<12} {'الوقت':<12} {'النتيجة':<10}{C.RESET}")
        print(f"  {C.BOLD}{'☠' * 62}{C.RESET}")

        for r in results:
            name = f"{r['icon']} {r['name']}"
            if r['accessible']:
                status = f"{C.GREEN}{r['status']}{C.RESET}"
                time_str = f"{C.PURPLE}{r['time']}ms{C.RESET}"
                result = f"{C.GREEN}{C.BOLD}✅ مفتوح{C.RESET}"
            else:
                status = f"{C.RED}{r['status']}{C.RESET}"
                time_str = f"{C.RED}---{C.RESET}"
                result = f"{C.RED}{C.BOLD}❌ محظور{C.RESET}"

            print(f"  {C.WHITE} {name:<28} {status:<22} {time_str:<22} {result}")

        print(f"  {C.BOLD}{'☠' * 62}{C.RESET}")

        # Summary
        print()
        total = len(results)
        percent = (accessible / total * 100) if total > 0 else 0

        if percent >= 80:
            bar_color = C.GREEN
            status_icon = "🟢"
        elif percent >= 50:
            bar_color = C.GOLD
            status_icon = "🟡"
        else:
            bar_color = C.RED
            status_icon = "🔴"

        print(f"  {status_icon} {C.BOLD}الملخص:{C.RESET}")
        print(f"  {C.GREEN}   ✅ مواقع مفتوحة: {accessible}/{total}{C.RESET}")
        print(f"  {C.RED}   ❌ مواقع محظورة: {blocked}/{total}{C.RESET}")

        bar_len = 40
        filled = int(bar_len * percent / 100)
        bar = f"{bar_color}{'█' * filled}{'░' * (bar_len - filled)}{C.RESET}"
        print(f"  {C.WHITE}   نسبة النجاح: [{bar}] {bar_color}{percent:.1f}%{C.RESET}")
        print()

        return accessible, blocked

    def display_ip_info(self, ip, details, label=""):
        """Display IP information beautifully"""
        print(f"  {C.PURPLE}╔{'═' * 50}╗{C.RESET}")
        print(f"  {C.PURPLE}║{C.BOLD}{C.WHITE}  {label:^48}{C.PURPLE}║{C.RESET}")
        print(f"  {C.PURPLE}╠{'═' * 50}╣{C.RESET}")
        print(f"  {C.PURPLE}║{C.WHITE}  🌐 IP: {C.GREEN}{ip:<39}{C.PURPLE}║{C.RESET}")

        if details:
            country = details.get('country', 'N/A')
            city = details.get('city', 'N/A')
            isp = details.get('isp', details.get('org', 'N/A'))[:35]
            region = details.get('regionName', details.get('region', 'N/A'))

            print(f"  {C.PURPLE}║{C.WHITE}  🏳️  البلد: {C.GOLD}{country:<35}{C.PURPLE}║{C.RESET}")
            print(f"  {C.PURPLE}║{C.WHITE}  🏙️  المدينة: {C.GOLD}{city:<33}{C.PURPLE}║{C.RESET}")
            print(f"  {C.PURPLE}║{C.WHITE}  📡 المنطقة: {C.GOLD}{region:<34}{C.PURPLE}║{C.RESET}")
            print(f"  {C.PURPLE}║{C.WHITE}  🔌 ISP: {C.GOLD}{isp:<38}{C.PURPLE}║{C.RESET}")

        print(f"  {C.PURPLE}╚{'═' * 50}╝{C.RESET}")

    # ═══════════════════════════════════════════
    #            MAIN OPERATIONS
    # ═══════════════════════════════════════════

    def full_unblock(self):
        """Full IP unblock process"""
        self.start_time = time.time()

        # Step 1: Get current IP
        print_section("🔍 الخطوة 1: تحليل IP الحالي")
        loading_animation("جاري الحصول على IP الحالي...", 2)
        self.original_ip, ip_data = self.get_current_ip()

        if self.original_ip:
            details = self.get_ip_details(self.original_ip)
            self.display_ip_info(self.original_ip, details, "🔒 IP الحالي (قبل فك الحظر)")
        else:
            print_error("فشل في الحصول على IP الحالي!")
            print_warning("تأكد من اتصالك بالإنترنت")
            return

        # Step 2: Initial website test
        print_section("🔍 الخطوة 2: فحص المواقع قبل فك الحظر")
        loading_animation("جاري فحص المواقع...", 1)
        before_results = self.test_all_websites()
        before_accessible, _ = self.display_results(before_results)

        # Step 3: DNS Flush
        print_section("🧹 الخطوة 3: تنظيف DNS Cache")
        loading_animation("جاري تنظيف ذاكرة DNS...", 2)
        flushed = self.flush_dns_cache()
        print_success(f"تم تنظيف DNS Cache ({flushed} عمليات)")

        # Step 4: Change DNS
        print_section("🔄 الخطوة 4: تغيير خوادم DNS")
        loading_animation("جاري تغيير DNS...", 2)

        best_dns = None
        best_time = float('inf')

        print_info("اختبار سرعة خوادم DNS...")
        for name, servers in DNS_SERVERS.items():
            try:
                start = time.time()
                socket.setdefaulttimeout(3)
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.connect((servers[0], 53))
                sock.close()
                elapsed = time.time() - start
                speed_bar = "█" * int(max(1, 20 - elapsed * 20))
                color = C.GREEN if elapsed < 0.1 else C.GOLD if elapsed < 0.3 else C.RED
                print(f"    {color}⚡ {name:<18} {servers[0]:<18} {elapsed*1000:.0f}ms  {speed_bar}{C.RESET}")
                if elapsed < best_time:
                    best_time = elapsed
                    best_dns = name
            except:
                print(f"    {C.RED}✗ {name:<18} {servers[0]:<18} غير متاح{C.RESET}")

        if best_dns:
            dns_name, dns_ips = self.change_dns(best_dns)
            print_success(f"تم اختيار أسرع DNS: {dns_name} ({dns_ips[0]}, {dns_ips[1]})")
        else:
            dns_name, dns_ips = self.change_dns("Cloudflare")
            print_warning(f"تم استخدام DNS الافتراضي: Cloudflare")

        # Step 5: MAC Address Spoofing
        print_section("🔀 الخطوة 5: تغيير MAC Address")
        loading_animation("جاري تغيير عنوان MAC...", 2)
        new_mac = self.spoof_mac_address()
        print_success(f"MAC Address جديد: {new_mac}")

        # Step 6: Reset Network
        print_section("📡 الخطوة 6: إعادة تعيين الشبكة")
        loading_animation("جاري إعادة تعيين واجهة الشبكة...", 2)
        self.reset_network_interface()
        print_success("تم إعادة تعيين الشبكة")

        # Step 7: Toggle Airplane Mode
        print_section("✈️  الخطوة 7: تبديل وضع الطيران (تغيير IP)")
        self.toggle_airplane_mode()
        loading_animation("جاري انتظار اتصال الشبكة...", 5)
        print_success("تم تبديل وضع الطيران")

        # Step 8: Refresh Session
        print_section("🔄 الخطوة 8: تجديد الجلسة")
        loading_animation("جاري تجديد معرفات الاتصال...", 2)
        self.session.cookies.clear()
        self.session.headers.update({'User-Agent': self.generate_user_agent()})
        print_success("تم تجديد User-Agent و Cookies")

        # Step 9: Get new IP
        print_section("🌐 الخطوة 9: التحقق من IP الجديد")
        loading_animation("جاري الحصول على IP الجديد...", 3)
        self.new_ip, new_data = self.get_current_ip()

        if self.new_ip:
            new_details = self.get_ip_details(self.new_ip)
            self.display_ip_info(self.new_ip, new_details, "🔓 IP الجديد (بعد فك الحظر)")

            if self.new_ip != self.original_ip:
                print_success(f"تم تغيير IP بنجاح! {self.original_ip} → {self.new_ip}")
            else:
                print_warning("IP لم يتغير - جرب تفعيل/إلغاء وضع الطيران يدوياً")
        else:
            print_error("فشل في الحصول على IP الجديد")
            print_warning("انتظر قليلاً وتأكد من الاتصال...")

        # Step 10: Re-test websites
        print_section("🔍 الخطوة 10: إعادة فحص المواقع بعد فك الحظر")
        loading_animation("جاري إعادة فحص المواقع...", 1)
        after_results = self.test_all_websites()
        after_accessible, after_blocked = self.display_results(after_results)

        # ═══════════════════════════════════════════
        #           FINAL REPORT
        # ═══════════════════════════════════════════
        elapsed_total = time.time() - self.start_time

        print(f"\n  {C.GOLD}{'☠' * 58}{C.RESET}")
        print(f"  {C.BOLD}{C.WHITE}{'📋 التقرير النهائي':^52}{C.RESET}")
        print(f"  {C.GOLD}{'☠' * 58}{C.RESET}")

        print(f"""
  {C.WHITE}  🔒 IP القديم:        {C.RED}{self.original_ip or 'غير معروف'}{C.RESET}
  {C.WHITE}  🔓 IP الجديد:        {C.GREEN}{self.new_ip or 'غير معروف'}{C.RESET}
  {C.WHITE}  📡 DNS المستخدم:     {C.PURPLE}{self.dns_selected or 'غير محدد'}{C.RESET}
  {C.WHITE}  🔀 MAC الجديد:       {C.PURPLE}{new_mac}{C.RESET}
  {C.WHITE}  ⏱️  الوقت المستغرق:  {C.GOLD}{elapsed_total:.1f} ثانية{C.RESET}

  {C.WHITE}  📊 المواقع قبل:      {C.RED}{before_accessible}/{len(before_results)} مفتوحة{C.RESET}
  {C.WHITE}  📊 المواقع بعد:      {C.GREEN}{after_accessible}/{len(after_results)} مفتوحة{C.RESET}
  {C.WHITE}  📈 التحسن:           {C.GREEN}+{after_accessible - before_accessible} مواقع{C.RESET}
        """)

        ip_changed = "✅ نعم" if (self.new_ip and self.new_ip != self.original_ip) else "❌ لا"
        print(f"  {C.WHITE}  🔄 هل تغير IP:      {C.GREEN if 'نعم' in ip_changed else C.RED}{ip_changed}{C.RESET}")

        if after_accessible >= len(after_results) * 0.8:
            print(f"\n  {C.BG_GREEN}{C.WHITE}{C.BOLD}  🎉 تم فك الحظر بنجاح! معظم المواقع تعمل الآن  {C.RESET}")
        elif after_accessible > before_accessible:
            print(f"\n  {C.GOLD}{C.BOLD}  ⚡ تحسن جزئي - جرب إعادة تشغيل الأداة مرة أخرى  {C.RESET}")
        else:
            print(f"\n  {C.RED}{C.BOLD}  ⚠️  جرب تفعيل VPN أو تغيير الشبكة للحصول على نتائج أفضل  {C.RESET}")

        print(f"\n  {C.GOLD}{'☠' * 58}{C.RESET}\n")

    def quick_test(self):
        """Quick website accessibility test"""
        print_section("⚡ فحص سريع للمواقع")
        loading_animation("جاري الفحص السريع...", 1)
        results = self.test_all_websites()
        self.display_results(results)

    def dns_only(self):
        """Change DNS only"""
        print_section("🔄 تغيير DNS فقط")

        print(f"\n  {C.BOLD}اختر خادم DNS:{C.RESET}\n")
        dns_list = list(DNS_SERVERS.keys())
        for i, name in enumerate(dns_list, 1):
            servers = DNS_SERVERS[name]
            print(f"    {C.PURPLE}[{i}]{C.WHITE} {name:<18} ({servers[0]}, {servers[1]}){C.RESET}")
        print(f"    {C.PURPLE}[0]{C.WHITE} اختيار تلقائي (الأسرع){C.RESET}")

        try:
            choice = int(input(f"\n  {C.GOLD}➤ اختيارك: {C.RESET}"))
            if choice == 0:
                dns_name, dns_ips = self.change_dns()
            elif 1 <= choice <= len(dns_list):
                dns_name, dns_ips = self.change_dns(dns_list[choice - 1])
            else:
                print_error("اختيار غير صحيح!")
                return
        except:
            print_error("إدخال غير صحيح!")
            return

        self.flush_dns_cache()
        print_success(f"تم تغيير DNS إلى: {dns_name} ({dns_ips[0]}, {dns_ips[1]})")

        loading_animation("جاري فحص المواقع...", 2)
        results = self.test_all_websites()
        self.display_results(results)

    def show_ip_info(self):
        """Show current IP information"""
        print_section("🌐 معلومات IP الحالي")
        loading_animation("جاري الحصول على المعلومات...", 2)

        ip, data = self.get_current_ip()
        if ip:
            details = self.get_ip_details(ip)
            self.display_ip_info(ip, details, "معلومات IP الحالي")

            # Extra details
            if details:
                print(f"\n  {C.WHITE}  📍 الإحداثيات: {C.PURPLE}{details.get('lat', 'N/A')}, {details.get('lon', 'N/A')}{C.RESET}")
                print(f"  {C.WHITE}  🕐 المنطقة الزمنية: {C.PURPLE}{details.get('timezone', 'N/A')}{C.RESET}")
                print(f"  {C.WHITE}  📮 الرمز البريدي: {C.PURPLE}{details.get('zip', 'N/A')}{C.RESET}")
                print(f"  {C.WHITE}  🏢 المنظمة: {C.PURPLE}{details.get('org', 'N/A')}{C.RESET}")
                print(f"  {C.WHITE}  📡 AS: {C.PURPLE}{details.get('as', 'N/A')}{C.RESET}")
                print()
        else:
            print_error("فشل في الحصول على معلومات IP!")


# ═══════════════════════════════════════════
#              MAIN MENU
# ═══════════════════════════════════════════

def main():
    tool = IPUnblockTool()

    while True:
        banner()
        print(f"""
  {C.BOLD}{C.WHITE}  اختر العملية المطلوبة:{C.RESET}

    {C.GREEN}[1]{C.WHITE} 🚀 فك الحظر الكامل (تلقائي)      {C.DIM}- الأكثر فعالية{C.RESET}
    {C.GREEN}[2]{C.WHITE} ⚡ فحص سريع للمواقع               {C.DIM}- فحص فقط{C.RESET}
    {C.GREEN}[3]{C.WHITE} 🔄 تغيير DNS فقط                  {C.DIM}- سريع{C.RESET}
    {C.GREEN}[4]{C.WHITE} 🌐 عرض معلومات IP                 {C.DIM}- معلومات{C.RESET}
    {C.GREEN}[5]{C.WHITE} ✈️  تبديل وضع الطيران              {C.DIM}- تغيير IP{C.RESET}
    {C.GREEN}[6]{C.WHITE} 🔀 تغيير MAC Address              {C.DIM}- متقدم{C.RESET}
    {C.RED}[0]{C.WHITE} 🚪 خروج{C.RESET}

  {C.GOLD}{'☠' * 50}{C.RESET}
        """)

        try:
            choice = input(f"  {C.GOLD}{C.BOLD}➤ اختيارك: {C.RESET}")
        except (KeyboardInterrupt, EOFError):
            print(f"\n\n  {C.GOLD}👋 إلى اللقاء!{C.RESET}\n")
            sys.exit(0)

        if choice == '1':
            tool.full_unblock()
        elif choice == '2':
            tool.quick_test()
        elif choice == '3':
            tool.dns_only()
        elif choice == '4':
            tool.show_ip_info()
        elif choice == '5':
            print_section("✈️  تبديل وضع الطيران")
            tool.toggle_airplane_mode()
            loading_animation("جاري إعادة الاتصال...", 5)
            ip, _ = tool.get_current_ip()
            if ip:
                print_success(f"IP الحالي: {ip}")
            else:
                print_warning("انتظر حتى يعود الاتصال...")
        elif choice == '6':
            print_section("🔀 تغيير MAC Address")
            new_mac = tool.spoof_mac_address()
            print_success(f"MAC Address الجديد: {new_mac}")
        elif choice == '0':
            print(f"\n  {C.GOLD}👋 شكراً لاستخدام الأداة! إلى اللقاء!{C.RESET}\n")
            sys.exit(0)
        else:
            print_error("اختيار غير صحيح!")

        input(f"\n  {C.DIM}⏎ اضغط Enter للمتابعة...{C.RESET}")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n  {C.GOLD}👋 تم الإيقاف. إلى اللقاء!{C.RESET}\n")
        sys.exit(0)