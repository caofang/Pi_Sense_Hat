# Fang 2020/12/22

PKG_VERSION=1
PKG_DIR=fc_led_animation_$(PKG_VERSION)
DEBIAN_DIR=DEBIAN/


build:	
	echo "Creating deb package..."
	mkdir -p $(PKG_DIR)/usr/bin/
	mkdir -p $(PKG_DIR)/tmp/

	cp src/led_animation.py $(PKG_DIR)/usr/bin/led_animation.py
	cp -R src/DEBIAN $(PKG_DIR)
	cp src/fc_led_animation.service $(PKG_DIR)/tmp/

	chmod +x $(PKG_DIR)/DEBIAN/preinst
	chmod +x $(PKG_DIR)/DEBIAN/postinst

	dpkg-deb -b $(PKG_DIR)

uninstall:
	echo "Removing existing installation"
	sudo apt autoremove -y fc-led-animation

install:
	echo "Installing new package"
	sudo apt install -y ./$(PKG_DIR).deb

reinstall:
	$(MAKE) uninstall
	$(MAKE) install

clean:
	echo "cleaning..."
	rm *.deb
	$(MAKE) -C src PKG_VERSION=$(PKG_VERSION) clean
