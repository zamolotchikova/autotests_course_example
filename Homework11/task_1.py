# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

sbis_ru = 'https://sbis.ru'
tensor_about = 'https://tensor.ru/about'
driver = webdriver.Chrome()
try:
    driver.get(sbis_ru)
    Contacts = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item [href="/contacts"]')
    Contacts.click()
    sleep(2)
    tensor = driver.find_element(By.CSS_SELECTOR, '[id="contacts_clients"] [href="https://tensor.ru/"]')
    tensor.click()
    sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    sleep(3)
    main_tensor = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-Index__card-title')
    main_tensor.location_once_scrolled_into_view
    assert main_tensor.is_displayed()
    about_tensor = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__card-text [href="/about"]')
    about_tensor.click()
    assert driver.current_url == tensor_about

finally:
    driver.quit()
