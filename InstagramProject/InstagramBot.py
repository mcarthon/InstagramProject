if __name__ == "__main__":

	from selenium import webdriver;
	from selenium.webdriver.support.wait import WebDriverWait;
	from selenium.webdriver.common.by import By;
	from selenium.webdriver.support import expected_conditions as EC
	from selenium.webdriver.firefox.options import Options;
	from selenium.webdriver.firefox.service import Service;
	from selenium.webdriver.common.proxy import Proxy, ProxyType;

	from webdriver_manager.firefox import GeckoDriverManager;

	import os;
	import time;
	import random;

	from variables import *

	proxy = Proxy ({

			"proxyType" : ProxyType.MANUAL,
			"httpProxy" : random.choice ( PROXY_LIST ),
			"sslProxy"  : random.choice ( PROXY_LIST )

		});
	print(f"Proxy: {proxy}");

	 # Print the firefox path to ensure it's correct
	print(f"Using Firefox binary at: {firefox_path}");

	# Check if the file exists at the specified path
	if not os.path.isfile(firefox_path):
		print(f"Firefox binary not found at {firefox_path}");
	else:
		print(f"Firefox binary found at {firefox_path}");

	user_agent = USER_AGENTS[3];
	print(f"User Agent: {user_agent}");

	options = Options();
	options.log.level = "trace";
	options.proxy = proxy;
	options.set_preference ( "general.useragent.override", user_agent );
	options.binary_location = firefox_path;

	service = Service ( GeckoDriverManager().install(), log_path = 'geckodriver.log' );

	try:
		driver = webdriver.Firefox(service=service, options=options)
		driver.get("https://ww.instagram.com")
		print("Firefox opened successfully")
		driver.quit()
	except Exception as e:
		print(f"Error occurred: {e}")
		raise
		driver.quit();

	driver.get("https://www.instagram.com");
	
	wait = WebDriverWait(driver, timeout = 10);

	wait.until(EC.element_to_be_clickable((By.XPATH, username_xpath)));

	username = driver.find_element(By.XPATH, value = username_xpath);
	password = driver.find_element(By.XPATH, value = password_xpath);
	log_in   = driver.find_element(By.XPATH, value = log_in_xpath);

	wait.until(lambda x: username.is_displayed());

	username.click();

	for letter in USERNAME:

		username.send_keys ( letter );

		time.sleep ( random.uniform ( 0.5, 1.5 ) );

	password.click();

	for letter in PASSWORD:

		password.send_keys ( letter );

		time.sleep ( random.uniform ( 0.5, 1.5 ) );

	log_in.click();

	time.sleep ( random.uniform ( 2, 4 ) );

	driver.quit();