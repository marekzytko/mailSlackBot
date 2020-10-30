## Mail Notification Slack Bot

### How to use?
You will need:
- Generated **Slack's Appliaction**
- **Bot User OAuth Access Token**
- **Chat:Write:Bot** OAuth Scope
- Mail account which uses **IMAP4**
-------------------------------
### **CentOS**

You may encounter problems when installing slack dependencies using pip3. You may have troubles installing one of them, i.e.:

**fatal error: python.h no such file or directory**

If so, you have to upgrade GCC, enable continuous release repositories and install python3-devel package.

```
sudo yum --enablerepo=cr update
sudo yum install python3-devel
```
In order to enable continuous release repositories for python3, you may need to remove python3 at all first

### **Debian**

By analogy - complete instructions coming soon
