function RunSentimentAnalysis() {
    const textToAnalyze = document.getElementById("textToAnalyze").value.trim();
    const resultElement = document.getElementById("system_response");

    if (!textToAnalyze) {
        resultElement.textContent = "Please enter some text to analyze.";
        return;
    }

    const xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState === 4) {
            if (this.status === 200) {
                resultElement.textContent = this.responseText;
            } else {
                resultElement.textContent =
                    this.responseText || "Unable to analyze the text. Please try again.";
            }
        }
    };

    xhttp.open(
        "GET",
        "/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze),
        true
    );

    xhttp.send();
}