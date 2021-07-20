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
        let data = await resp.json()
        window.location.pathname = `/question/${data.id}`
    }
</script>

<main>
    <div class="container">
        <h1 class="title">New Question</h1>
        <div class="container">
            <input type="text" bind:value={title} placeholder="Epic title...">
            <p class="help">Title</p>
            <br>
            <input type="text" bind:value={body} placeholder="Epic body">
            <p class="help">Body</p>
            <br>
            <button class="button is-info" on:click={create_question}>Create</button>
        </div>
    </div>
</main>