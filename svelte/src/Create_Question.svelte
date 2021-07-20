<script>
    import { getCookie } from './helpers/helpers'
    let title, body;
    
    async function create_question(){
        let resp = await fetch('/api/v1/question/', {
            method: "POST",
            headers: {
                "X-CSRFToken": getCookie('csrftoken'),
                "Content-Type": "application/json"
            },
            mode: "same-origin",
            body: JSON.stringify({
                "title": title,
                "body": body
            })
        })
        if (resp.ok) {
            let data = await resp.json()
            window.location.pathname = `/question/${data.id}`
            return;
        }
        alert("There was an error with your form.")

    }
</script>

<main>
    <div class="container">
        <h1 class="title">New Question</h1>
        <div class="container">
            <input type="text" bind:value={title} placeholder="Epic title..." class="input {!!title ? "" : "is-danger"}">
            <p class="help">Title {!!title? "" : "| Fill out this field"}</p>
            <br>
            <textarea type="text" bind:value={body} placeholder="Epic body" class="textarea {!!body ? "" : "is-danger"}"></textarea>
            <p class="help">Body {!!body? "" : "| Fill out this field"}</p>
            <br>
            <button class="button is-info" on:click={create_question}>Create</button>
        </div>
    </div>
</main>