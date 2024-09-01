# ML: Storybook Reading Level Predictor

> 🤖📚 Machine learning model which predicts the reading level of a storybook.

This machine learning model is used by the [webapp](https://github.com/elimu-ai/webapp) for predicting the [reading level](https://github.com/elimu-ai/model/blob/main/src/main/java/ai/elimu/model/v2/enums/ReadingLevel.java) of a storybook. The reading level is based on various metrics indicating the books difficulty level, e.g. its total number of words.

> [!IMPORTANT]
> The webapp where the machine learning model is used is built with Java, so the machine learning code needs to export the model in a file format supported by Java web applications.

## Code Usage

Prerequisites:

- Install [Python](https://www.python.org/)

### Working directory

Change your working directory to [`pmml`](./pmml):

```bash
cd pmml
```

### Dependencies

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

### Test

Run the unit tests:

```bash
pytest
```

### Run

Run all steps (1-3):

```bash
python run_all_steps.py
```

---

<p align="center">
  <img src="https://github.com/elimu-ai/webapp/blob/main/src/main/webapp/static/img/logo-text-256x78.png" />
</p>
<p align="center">
  elimu.ai - Free open-source learning software for out-of-school children 🚀✨
</p>
<p align="center">
  <a href="https://elimu.ai">Website 🌐</a>
  &nbsp;•&nbsp;
  <a href="https://github.com/elimu-ai/wiki#readme">Wiki 📃</a>
  &nbsp;•&nbsp;
  <a href="https://github.com/orgs/elimu-ai/projects?query=is%3Aopen">Projects 👩🏽‍💻</a>
  &nbsp;•&nbsp;
  <a href="https://github.com/elimu-ai/wiki/milestones">Milestones 🎯</a>
  &nbsp;•&nbsp;
  <a href="https://github.com/elimu-ai/wiki#open-source-community">Community 👋🏽</a>
  &nbsp;•&nbsp;
  <a href="https://www.drips.network/app/drip-lists/41305178594442616889778610143373288091511468151140966646158126636698">Support 💜</a>
</p>
