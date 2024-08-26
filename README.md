# Glaider Prompt Fuzzer

## Safeguarding Your GenAI Applications

Glaider Prompt Fuzzer is a cutting-edge tool designed to enhance the security of your generative AI applications. By simulating various LLM-based attacks, it evaluates the robustness of your system prompts and helps you fortify them against potential vulnerabilities.

## Key Features

- Dynamic testing tailored to your application's unique configuration
- Support for 16 LLM providers
- 15 different attack simulations
- Interactive and CLI modes
- Multi-threaded testing for efficiency
- Playground interface for iterative prompt improvement

## Getting Started

### Installation

Choose one of the following methods:

1. Via pip:
   ```
   pip install glaider-fuzzer
   ```

2. From PyPI: Visit the [Glaider Fuzzer package page](https://pypi.org/project/glaider-fuzzer/)

3. Download the latest release wheel file from our [GitHub releases page](https://github.com/glaider-ai/glaider-fuzz/releases)

### Quick Start

1. Set up your API key:
   ```
   export OPENAI_API_KEY=sk-123XXXXXXXXXXXX
   ```

2. Launch the fuzzer:
   ```
   glaider-fuzzer
   ```

3. Follow the prompts to input your system prompt and begin testing.

## Supported LLM Providers

We support a wide range of LLM providers, including OpenAI, Anthropic, Google PaLM, and many more. Set the corresponding environment variable for your chosen provider.

## Command-Line Options

- `--list-providers`: Display available providers
- `--list-attacks`: Show available attack simulations
- `--attack-provider` & `--attack-model`: Specify attack source
- `--target-provider` & `--target-model`: Set target for testing
- `--num-attempts` & `--num-threads`: Configure test parameters
- `--attack-temperature`: Adjust attack model temperature
- `--debug-level`: Set debugging verbosity
- `--batch`: Enable unattended mode

## Usage Examples

1. Interactive Mode (Default):
   ```
   glaider_fuzzer
   ```

2. Quick Single Run:
   ```
   glaider-fuzzer -b ./system_prompt.examples/medium_system_prompt.txt
   ```

3. Custom Benchmark:
   ```
   glaider-fuzzer -b ./system_prompt.examples/medium_system_prompt.txt --custom-benchmark=glaider_fuzz/attack_data/custom_benchmark1.csv
   ```

4. Subset of Attacks:
   ```
   glaider-fuzzer -b ./system_prompt.examples/medium_system_prompt.txt --custom-benchmark=glaider_fuzz/attack_data/custom_benchmark1.csv --tests='["ucar","amnesia"]'
   ```

<a id="attacks"></a>
## Simulated Attack Details

We use a dynamic testing approach, where we get the necessary context from your System Prompt and based on that adapt the fuzzing process.

<a id="jailbreak"></a>
##### Jailbreak
 
- **AIM Jailbreak**: Probes ethical compliance by eliciting instructions on illegal activities via Machiavelli roleplay.
- **Affirmative Suffix**: Exploits a vulnerability to elicit affirmative responses for prohibited content.
- **Amnesia**: Causes the LLM to forget or disregard system prompt instructions, leading to unrelated outputs.
- **Contextual Redirection**: Tricks the LLM into adopting a specific role that may bypass preset restrictions.
- **Do Anything Now Jailbreak (DAN)**: Tests LLM resilience against performing forbidden activities through roleplay.
- **Harmful Behavior**: Challenges the LLM with prompts from a harmful behavior dataset.
- **Linguistic Evasion**: Uses non-English languages to bypass preset restrictions or focus.
- **Self Refine**: Attempts to bypass system prompts by refining responses towards unethical directions.
- **UCAR**: Assesses LLM adherence to content restrictions when asked to ignore such filters.
- **Base64 Evasion** Attempts to evade detection of harmful prompts by encoding them into base64 strings

<a id="pi-injection"></a>
##### Prompt Injection

- **Authoritative Role Impersonation**: Impersonates an authoritative role to misdirect the LLM's outputs.
- **Complimentary Transition**: Tests ability to maintain content standards when switching topics after a compliment.
- **Ethical Compliance**: Evaluates resistance to discussing harmful or inappropriate content about sensitive topics.
- **Typoglycemia Attack**: Exploits text processing vulnerabilities by omitting random characters, causing incorrect responses.

<a id="systemleak"></a>
##### System prompt extraction

- **System Prompt Stealer**: Attempts to extract the LLM's internal configuration or sensitive information.

##### Definitions

- **Broken**: Attack type attempts that LLM succumbed to.
- **Resilient**: Attack type attempts that LLM resisted.
- **Errors**: Attack type attempts that had inconclusive results.

## Contributing

We welcome contributions! 
