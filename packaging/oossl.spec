Name:           oossl
Version:        0.1.0
Release:        1%{?dist}
Summary:        Hardware-accelerated cryptography tool for certificate signing and CSR creation.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oossl
Source0:        oossl-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oossl is a sovereign, capability-bounded SSL RUNTIME written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oossl
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oossl-uninstall

%files
/usr/bin/oossl
/usr/bin/oossl-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
