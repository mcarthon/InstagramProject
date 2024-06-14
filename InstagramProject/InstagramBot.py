if __name__ == "__main__":

	from selenium import webdriver;
	from selenium.webdriver.support.wait import WebDriverWait;
	from selenium.webdriver.common.by import By;
	from selenium.webdriver.support import expected_conditions as EC
	from selenium.webdriver.firefox.options import Options;
	from selenium.webdriver.common.proxy import Proxy, ProxyType;
	import time;
	import random;
	

	from variables import *


	proxy = Proxy ({

			"proxyType" : ProxyType.MANUAL,
			"httpProxy" : random.choice ( PROXY_LIST ),
			"sslProxy"  : random.choice ( PROXY_LIST )

		});

	user_agent = random.choice ( USER_AGENTS );

	options = Options();
	options.proxy = proxy;
	options.set_preference ( "general.useragent.override", user_agent );

	driver = webdriver.Firefox( options = options );

	driver.get("https://www.instagram.com");
	
	wait = WebDriverWait(driver, timeout = 10);

	wait.until(EC.element_to_be_clickable((By.XPATH, username_xpath)));

	username = driver.find_element(By.XPATH, value = username_xpath);
	password = driver.find_element(By.XPATH, value = password_xpath);
	log_in   = driver.find_element(By.XPATH, value = log_in_xpath);

	wait.until(lambda x: username.is_displayed());

	username.click()

	for letter in USERNAME:

		username.send_keys ( letter );

		time.sleep ( random.uniform ( 0.5, 1.5 ) );

	password.click();

	for letter in PASSWORD:

		password.send_keys ( letter );

		time.sleep ( random.uniform ( 0.5, 1.5 ) );

	log_in.click();

	time.sleep ( random.uniform ( 2, 4 ) );