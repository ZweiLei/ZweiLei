def admin_command(command: list, sudo=True):
    if sudo:
        return ["sudo"] + command
    return command


class TestAdminCommand:
    def command(self):
        return ["ps", "aux"]
    
    def test_no_sudo(self):
        result = admin_command(self.command(), sudo=False)
        assert result == self.command()

    def test_sudo(self):
        result = admin_command(self.command(), sudo=True)
        expected = ["sudo"] + self.command()
        assert result == expected
