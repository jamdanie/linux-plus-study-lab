# Build a boot link without changing the host

A systemd unit describes work for the service manager. For this lab, enabling a service creates a link under the target named by WantedBy. You can see the link appear without booting a VM. Use Linux with Bash and systemctl installed. Run the whole block in one shell. The explicit --root points every systemctl command at a new temporary directory.

```bash
lab=$(mktemp -d)
mkdir -p "$lab/etc/systemd/system"
printf '%s\n' '[Unit]' 'Description=Practice target' > "$lab/etc/systemd/system/multi-user.target"
cat > "$lab/etc/systemd/system/rack-report.service" <<'EOF'
[Unit]
Description=Practice rack report
[Service]
Type=oneshot
ExecStart=/bin/true
[Install]
WantedBy=multi-user.target
EOF
systemctl --root="$lab" enable rack-report.service
systemctl --root="$lab" is-enabled rack-report.service
ls -l "$lab/etc/systemd/system/multi-user.target.wants/"
systemctl --root="$lab" disable rack-report.service
systemctl --root="$lab" is-enabled rack-report.service
```

Expect enabled, a link named rack-report.service, then disabled. The final status query returns a nonzero exit code for disabled. The offline directory has no running service manager. This exercise changes installation links only. If your terminal has no systemctl, use the [reboot ticket](../games/service-reboot.md) to read the same distinction from supplied evidence.

[systemctl manual](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html)
