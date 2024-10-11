document.addEventListener("DOMContentLoaded", function () {
  const fromLanguageElement = document.querySelector("#from-language");
  const toLanguageElement = document.querySelector("#to-language");
  const inputElement = document.querySelector("#text-input");
  const imageInputElement = document.querySelector("#image");
  const outputElement = document.querySelector(".output");
  const submitElement = document.querySelector(".submit");

  submitElement.addEventListener("click", () => {
    const fromLanguageValue = fromLanguageElement.value;
    const toLanguageValue = toLanguageElement.value;

    if (imageInputElement.files.length > 0) {
      const imageFile = imageInputElement.files[0];
      const formData = new FormData();
      formData.append("image", imageFile);
      formData.append("from", fromLanguageValue);
      formData.append("to", toLanguageValue);

      axios
        .post("/translate/", formData)
        .then((response) => {
          inputElement.value = response.data.input;
          outputElement.value = response.data.output;
        })
        .catch((error) => {
          alert(error.response.data.error);
        });
    } else {
      const data = {
        input: inputElement.value.trim(),
        from: fromLanguageValue,
        to: toLanguageValue,
      };

      axios
        .post("/translate/", data)
        .then((response) => {
          inputElement.value = response.data.input;
          outputElement.value = response.data.output;
        })
        .catch((error) => {
          alert(error.response.data.error);
        });
    }
  });
});
