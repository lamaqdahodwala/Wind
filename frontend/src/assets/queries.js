export let queries = {
    all_questions: "{\n  allQuestions{\n    title\n    body\n    id \n}\n}",
    single_question: "query GetSingleQuestion($pk:Int){\n  singleQuestion(pk:$pk){\n    title\n    body\n    user{\n      username\n    }\n    answers{\n      content\n      user{\n        username\n        id\n      }\n    }\n  }\n}"
}
