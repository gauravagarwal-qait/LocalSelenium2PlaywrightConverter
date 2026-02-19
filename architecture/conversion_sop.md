# 📜 SOP: Selenium to Playwright Logic Mapping

## 🎯 Goal
Provide a deterministic mapping between Selenium Java commands and Playwright TypeScript to guide the LLM and the conversion tool.

## 🛠️ Mapping Rules

### 1. Basic Navigation
| Selenium Java | Playwright TS |
| :--- | :--- |
| `driver.get(url)` | `await page.goto(url)` |
| `driver.navigate().to(url)` | `await page.goto(url)` |
| `driver.getTitle()` | `await page.title()` |
| `driver.getCurrentUrl()` | `page.url()` |

### 2. Element Locators
| Selenium Java | Playwright TS |
| :--- | :--- |
| `By.id("foo")` | `page.locator('#foo')` |
| `By.className("foo")` | `page.locator('.foo')` |
| `By.name("foo")` | `page.locator('[name="foo"]')` |
| `By.cssSelector("foo")` | `page.locator('foo')` |
| `By.xpath("//foo")` | `page.locator('xpath=//foo')` |
| `By.linkText("foo")` | `page.getByRole('link', { name: 'foo' })` |

### 3. Actions
| Selenium Java | Playwright TS |
| :--- | :--- |
| `element.click()` | `await element.click()` |
| `element.sendKeys("text")` | `await element.fill("text")` |
| `element.clear()` | `await element.fill('')` |
| `element.getText()` | `await element.textContent()` |
| `element.getAttribute("attr")` | `await element.getAttribute("attr")` |

### 4. Waits & Assertions
| Selenium Java | Playwright TS |
| :--- | :--- |
| `WebDriverWait.until(...)` | Playwright auto-waits, or `await page.waitForSelector()` |
| `Assert.assertEquals(a, b)` | `await expect(locator).toHaveText(b)` |
| `Assert.assertTrue(element.isDisplayed())` | `await expect(locator).toBeVisible()` |

## 🧩 Structure (POM)
If the source code defines a class (e.g., `LoginPage`), the converted code should be a TypeScript class with `readonly page: Page` in the constructor.
