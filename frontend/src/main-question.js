import Question from './Question.svelte';

const question = new Question({
	target: document.getElementById("question-target"),
	props: JSON.parse(document.getElementById("question-props").textContent),
});

export default question;