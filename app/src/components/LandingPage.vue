<template>
  <v-container>
    <v-layout
      text-xs-center
      wrap
    >
      <v-flex xs12>
        <v-img
          :src="require('../assets/logo.svg')"
          class="my-3"
          contain
          height="200"
        />
        <TypingText
          text="Under Construction."
          class="typingText"
        />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
    import TypingText from './TypingText'

    export default {
        name: 'LandingPage',
        components: {
            TypingText,
        },
        props: {}
    }
</script>

<style>
    .typingText {
        margin-top: 5em;
    }
</style>