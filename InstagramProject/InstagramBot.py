if __name__ == "__main__":

	from selenium import webdriver;
	from selenium.webdriver.support.wait import WebDriverWait;
	from selenium.webdriver.common.by import By;
	from selenium.webdriver.support import expected_conditions as EC
	from selenium.webdriver.firefox.options import Options;

	from credentials import USERNAME, PASSWORD;
	import list_of_xpaths as xpaths;

	options = Options();
	options.set_preference("detach", True);

	driver = webdriver.Firefox(options = options);

	driver.get("https://www.instagram.com");
	
	wait = WebDriverWait(driver, timeout = 2);

	wait.until(EC.element_to_be_clickable((By.XPATH, xpaths.username_xpath)));

	username = driver.find_element(By.XPATH, value = xpaths.username_xpath);
	password = driver.find_element(By.XPATH, value = xpaths.password_xpath);
	log_in = driver.find_element(By.XPATH, value = xapths.log_in_xpath);

	wait.until(lambda x: username.is_displayed());

	username.click()

	driver.send_keys(USERNAME);

	password.click();

	driver.send_keys(PASSWORD);

	log_in.click();