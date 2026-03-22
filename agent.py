from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3",num_predict=2048, temperature=0.2)
cache={}
def generate_test_script(test_steps, actual, expected):
    key = test_steps + actual + expected
    if key in cache:
        return cache[key]

    prompt = f"""
    You are a QA Automation Engineer.

    Convert the following test steps into:
    - Selenium Java code
    - Cucumber feature file
    - TestNG assertions
    - Follow Page Object Model
    - Use WebDriverWait
    - Use try-catch
    - Generate clean readable code

    Test Steps:
    {test_steps}

    Actual Value: {actual}
    Expected Value: {expected}

    Include:
    - Wait conditions
    - Exception handling
    - Proper locators
    """

    return llm.invoke(prompt)


def analyze(actual, expected):
    if actual == expected:
        return "Test Passed ✅"
    else:
        return "Test Failed ❌"


def suggest_fix_ai(test_steps, actual, expected):
    prompt = f"""
        You are a senior QA Automation Engineer.

        A test case has failed.

        Test Steps:
        {test_steps}

        Actual Result:
        {actual}

        Expected Result:
        {expected}

        Analyze the failure and provide:
        1. Possible reasons for failure
        2. Fix suggestions
        3. Improvements to test script
        4. Better locator or wait strategy

        Be precise and practical.
        """

    return llm.invoke(prompt)


def save_output(content):
    with open("outputs/test.txt", "w") as f:
        f.write(content)


if __name__ == "__main__":

    steps = """
    1. Open login page
    2. Enter username 'admin'
    3. Enter password '1234'
    4. Click login button
    5. Verify message 'Login Successful'
    """
    actual = "Login Failed"
    expected = "Login Successful"

    result = generate_test_script(
        steps, actual, expected)

    print("=== GENERATED SCRIPT ===")
    print(result)

    # 🔥 ANALYSIS
    status = analyze("Login Failed", "Login Successful")
    print("\n=== TEST RESULT ===")
    print(status)

    # 🔥 SUGGEST FIX IF FAILED
    if "Failed" in status:
        print("\n=== AI FIX SUGGESTIONS ===")
        fixes = suggest_fix_ai(steps, actual, expected)
        print(fixes)

    save_output(result)