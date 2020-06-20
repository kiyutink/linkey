<script>
  import { api } from "../lib/api";
  import Input from "./input.svelte";
  import copy from "copy-to-clipboard";
  let url;
  let shortUrl;
  let copied = false;
</script>

<style lang="scss">
  main {
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  h1 {
    font-weight: 500;
  }

  .container {
    width: 300px;
    display: flex;
    flex-direction: column;
  }

  form {
    display: flex;
    flex-direction: column;
  }

  button {
    margin-top: 5px;
    margin-bottom: 5px;
    height: 30px;
    border-radius: 5px;
    border: 1px solid cornflowerblue;
    background-color: transparent;
    cursor: pointer;
    font-size: 18px;
    outline: none;

    &:focus {
      box-shadow: 0 0 0 1px cornflowerblue;
    }
  }
</style>

<main>
  <div class="container">
    <h1>Shorten your link</h1>
    {#if !shortUrl}
      <form
        on:submit={e => {
          e.preventDefault();
          api
            .createLink({ originalUrl: url, hasRedirection: false })
            .then(({ data }) => {
              shortUrl = `${window.location.origin}/${data.shortUrl}`;
            });
        }}>
        <Input bind:value={url} />
        <button>Shorten</button>
      </form>
    {:else}
      <Input value={shortUrl} />
      <button
        disabled={copied}
        on:click={() => {
          copy(shortUrl);
          copied = true;
          setTimeout(() => (copied = false), 2000);
        }}>
        {#if copied}Copied!{:else}Copy to clipboard{/if}
      </button>
      <button
        on:click={() => {
          shortUrl = '';
          url = '';
        }}>
        Create a new link
      </button>
    {/if}
  </div>

</main>
