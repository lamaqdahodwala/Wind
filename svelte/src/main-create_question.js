import Create_Question from './Create_Question.svelte';

const create_question = new Create_Question({
	target: document.getElementById("create_question-target"),
	props: JSON.parse(document.getElementById("create_question-props").textContent),
});

export default create_question;