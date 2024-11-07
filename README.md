
# RAG and Intelligent Agents using Agency Swarm

This repo is based on the excellent and short [agency-swarm-tutorial by John Adojo](https://github.com/john-adeojo/agency_swarm_tutorial.git)

## Rag implementations

RAG examples have been added for:
* RAG using custom APIs
* RAG using custom SQL databases

## Prerequisities
* OpenAPI API key is needed
* Other keys are optional

## Gettings started

### Clone and Navigate to the Repository

1. **Clone the Repo:**
   ```bash
   git clone https://github.com/jensaug/agency_swarm_tutorial.git
   ```

2. **Navigate to the Repo:**
   ```bash
   cd agency_swarm_tutorial
   ```

3. **Create a Virtual Environment:**
   ```bash
   python -m venv .venv
   ```
   
4. **Activate the Virtual Environment:**
   ```bash
   source .venv/bin/activate
   ```

5. **Install Requirements:**
   ```bash
   pip install -r requirements.txt
   ```

## Configure API Keys

1. **Add environments manually OR create a file  `.env` looking like this:**
   ```bash
   ELECTRICITY_MAP_API_KEY="XXX"
   OPENAI_API_KEY="YYY"
   SERPER_DEV_API_KEY="ZZZ"
   ```

2. **Enter API Keys:**
   - **ElectricityMap API (free) key**: Get it from [Electricity Maps](https://www.electricitymaps.com/free-tier-api)
   - **Serper API (free) Key:** Get it from [serper.dev](https://serper.dev/)
   - **OpenAI API Key:** Get it from [OpenAI](https://openai.com/)

## Run Agency
```bash
python agency.py
```

## Example queries

To Manager:
```
List some research on voting turnout in the Sweden
```
To ElectrityExpert:
```
Tell me about energy consumption at Tiunda School
```
```
And Brasil?
```
To AccidentAnalyst:
```
On Titanic, how many embarked from each town?
```

## Note!
settings.json is automatomatically created by Agency Swarm.
