# 🔍 Findings & Research

## 🚀 Research Log
- **2026-02-19:** Project initialized. Verified `codellama:latest` is available in Ollama.
- **2026-02-19:** Research confirmed that no one-click conversion tool exists, but LLM-based approaches (like the one we are building) are the most effective.

## 💡 Discoveries
### Key Mapping Patterns (Selenium -> Playwright)
- `driver.get(url)` -> `await page.goto(url)`
- `findElement(By.id("id"))` -> `page.locator('#id')`
- `findElement(By.xpath("//xpath"))` -> `page.locator('xpath=//xpath')`
- `element.sendKeys("text")` -> `await element.fill("text")`
- `element.click()` -> `await element.click()`
- `WebDriverWait` -> Playwright has auto-wait, but `await page.waitForSelector()` can be used for explicit waits.
- `Assert.assertEquals` -> `await expect(locator).toHaveText()`

### System Prompt Strategy
- Must emphasize the asynchronous nature of Playwright (`async/await`).
- Must enforce TypeScript types.
- Should suggest Page Object Model (POM) restructuring.
- Default to `chromium` engine.

## ⚠️ Constraints & Risks
- Parsing Java code accurately requires a robust parser (e.g., Tree-sitter or RegEx patterns if simple).
- Mapping Selenium commands to Playwright equivalents (Locators, Actions, Assertions).
- Variable scoping and state management differences between Java and JS/TS.
