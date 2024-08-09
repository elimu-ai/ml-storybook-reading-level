# ML: Storybook Reading Level Predictor

> 🤖📚 Machine learning model which predicts the reading level of a storybook.

This machine learning model is used by the [webapp](https://github.com/elimu-ai/webapp) for predicting the [reading level](https://github.com/elimu-ai/model/blob/main/src/main/java/ai/elimu/model/v2/enums/ReadingLevel.java) of a storybook. The reading level is based on various metrics indicating the books difficulty level, e.g. its total number of words.

> [!IMPORTANT]
> The webapp where the machine learning model is used is built with Java, so the TensorFlow code needs to export the model in a file format supported by Java web applications.

## Code Usage

Prerequisites:

- Install [Python](https://www.python.org/)
- Install the Python dependencies:

  ```python
  pip install -r requirements.txt
  ```

### 1. Prepare Data

The [`storybooks.csv`](https://github.com/elimu-ai/webapp/blob/main/src/main/resources/db/content_PROD/hin/storybooks.csv) dataset contains the paragraphs of each storybook in the `chapters` column, stored in JSON format.

> [!TIP]
> If you want to explore the storybook chapters in a more readable format, you can copy the data from the `chapters` column into a tool like [JSON Lint](https://jsonlint.com/). Just remember to replace all double-quotes (`""`) with single-quotes (`"`) first.
> 
> <kbd>![](https://github.com/user-attachments/assets/e03132e1-f1fd-43ee-acd3-d17929a87639)</kbd>

Python command for preparing the data:

```python
python ./prepare_data.py
```

### 2. Train Model

Python command for training the model:

```python
TODO
```

### 3. Make Prediction

Python command for making a prediction:

```python
TODO
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
