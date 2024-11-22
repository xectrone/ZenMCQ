function addListItem(containerClass, inputClass, inputName) {
    const inputField = document.querySelector(`.${inputClass}`);
    const listContainer = document.querySelector(`.${containerClass}`);
    const value = inputField.value.trim();

    if (value) {
        // Calculate alphabetical index
        const index = listContainer.children.length;
        const alphabetIndex = String.fromCharCode(65 + index); // 'A' = 65 in ASCII

        const item = document.createElement("div");
        item.className = "list-item";
        item.innerHTML = `
            <div class="input-group">
                <span class="form-control">${alphabetIndex}. ${value}</span>
                <button type="button" class="btn btn-secondary" onclick="removeListItem(this)">X</button>
            </div>
            <input type="hidden" name="${inputName}[]" value="${value}">
        `;
        listContainer.appendChild(item);

        // Add button for correct answer selection
        const answersContainer = document.querySelector('.answers-container .answers-list');
        const answerButton = document.createElement('button');
        answerButton.type = "button";
        answerButton.className = "btn btn-outline-primary m-1";
        answerButton.textContent = alphabetIndex;
        answerButton.onclick = () => selectCorrectAnswer(answerButton, index);
        answersContainer.appendChild(answerButton);

        inputField.value = "";
    } else {
        alert("Please enter a valid value!");
    }
}

function removeListItem(button) {
    const item = button.closest(".list-item");
    const listContainer = item.parentNode;
    const index = Array.from(listContainer.children).indexOf(item);

    // Remove correct answer button
    const answersContainer = document.querySelector('.answers-container .answers-list');
    answersContainer.children[index].remove();

    // Remove the option
    item.remove();

    // Recalculate indices
    Array.from(listContainer.children).forEach((child, newIndex) => {
        const span = child.querySelector('.form-control');
        const originalText = span.textContent.split('. ')[1]; // Extract original text
        const newAlphabetIndex = String.fromCharCode(65 + newIndex); // New index
        span.textContent = `${newAlphabetIndex}. ${originalText}`;
        answersContainer.children[newIndex].textContent = newAlphabetIndex;
        answersContainer.children[newIndex].onclick = () => selectCorrectAnswer(answersContainer.children[newIndex], newIndex);
    });
}

function selectCorrectAnswer(button, index) {
    const correctAnswersField = document.querySelector('.answers-container input[name="correct_answers"]');
    let correctAnswers = JSON.parse(correctAnswersField.value || "[]");

    if (correctAnswers.includes(index)) {
        // If already selected, remove it
        correctAnswers = correctAnswers.filter((i) => i !== index);
        button.classList.remove('btn-primary');
        button.classList.add('btn-outline-primary');
    } else {
        // Add the index
        correctAnswers.push(index);
        button.classList.remove('btn-outline-primary');
        button.classList.add('btn-primary');
    }

    correctAnswersField.value = JSON.stringify(correctAnswers);
}
