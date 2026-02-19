# 📖 Project Constitution: Selenium Java to Playwright JS/TS Converter

## 🎯 Project Overview
**Mission:** Build a deterministic tool to convert Selenium Java test scripts into Playwright JavaScript/TypeScript.

## 🏗️ Architectural Invariants
- **Architecture Style:** A.N.T. (Architecture, Navigation, Tools)
- **Framework:** Playwright (JS/TS)
- **Source:** Selenium (Java)
- **Reliability:** Prioritize deterministic code generation over speed.

## 📊 Data Schemas

### Input (Selenium Java)
```json
{
  "source_code": "string",
  "file_name": "string (optional)",
  "language": "java",
  "framework": "selenium"
}
```

### Output (Playwright JS/TS)
```json
{
  "converted_code": "string",
  "output_path": "string",
  "language": "typescript",
  "framework": "playwright",
  "conversion_log": [
    {
      "type": "info | warning | error",
      "message": "string"
    }
  ]
}
```

## 📜 Behavioral Rules
1. **Model Selection:** Use Ollama (specifically `codellama` or `deepseek-coder` if available) for the conversion engine.
2. **TS-First:** Default all conversions to Playwright **TypeScript** (.ts) for robustness.
3. **POM Pattern:** Attempt to preserve or refactor into Page Object Model if the source Java looks like a page class.
4. **Deterministic Locators:** Map `By.id`, `By.cssSelector`, `By.xpath` to Playwright's `page.locator()` or specialized selectors.
5. **Self-Healing UI:** The UI should show real-time conversion progress and allow manual overrides.
6. **Local-First:** All processing must happen locally via Ollama; no external LLM calls unless explicitly requested.
7. **Error Handling:** If the LLM produces invalid syntax, the system must attempt a "Self-Anneal" (re-prompting the model with the error).

## 🛠️ Maintenance Log
- **2026-02-19:** Protocol 0 Initialization completed.
