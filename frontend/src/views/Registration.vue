<!-- eslint-disable -->
<template>
  <div class="form">
    <form v-on:submit="handleRegistration">
      <b-form-group
        id="input-group-1"
        label="Email address:"
        v-model="email"
        label-for="input-1"
        description="We'll never share your email with anyone else."
      >username
      <b-form-input
        id="input-1"
        v-model="email"
        type="text"
        required
        placeholder="Enter email"
      ></b-form-input>
      </b-form-group>

      <b-form-group> 
        <label for="text-password">Username</label>
          <b-form-input
        id="username"
        v-model="username"
        type="text"
        required
        placeholder="Username"
      ></b-form-input>
      </b-form-group>     

      <b-form-group>
        <label for="text-password">Password</label>
        <b-input
          type="password"
          id="text-password"
          v-model="password"
          aria-describedby="password-help-block"></b-input>
      </b-form-group>

      <b-form-group>
        <label for="text-password">Confirm Password</label>
        <b-input
          type="password"
          id="text-password2"
          v-model="password2"
          aria-describedby="password-help-block"></b-input>
      </b-form-group> 
      <b-form-group> 
        <label for="text-password">First Name</label>
        <b-form-input
          id="input-2"
          v-model="firstName"
          type="text"
          required
          placeholder="Enter First Name"
        >
        </b-form-input>
      </b-form-group> 

      <b-form-group> 
        <label for="text-password">Last Name</label>
          <b-form-input
        id="input-3"
        v-model="lastName"
        type="text"
        required
        placeholder="Enter Last Name"
      ></b-form-input>
      </b-form-group>     
      <b-button type="submit" variant="primary">Register</b-button>
    </form>
  </div>
</template>

<script>
/* eslint-disable */
import { mapActions } from 'vuex';

export default {
  name: 'RegistrationForm',
  data() {
    return {
      email: '',
      username: '',
      password: '',
      password2: '',
      firstName: '',
      lastName: '',
      nextPath: '/login',
      errorMessage: '',
    };
  },
  mounted() {
    this.updateAfterNextPath();
  },
  methods: {
    handleRegistration(event) {
      event.preventDefault();
      // if (this.password != this.password2){
      //   pass 
      //   // Disable register button
      // }
      this.register({ 
        username: this.username,
        password: this.password,
        password2: this.password2,
        firstName: this.firstName,
        lastName: this.lastName,
        email: this.email
        })
        .then(() => {
          this.$router.push(this.nextPath);
        });
    },
    updateAfterNextPath() {
      if ('next' in this.$route.query) {
        this.nextPath = this.$route.query.next;
      }
    },
    ...mapActions([
      'register',
    ]),
  },
};
</script>

<style scoped>
form {
  max-width:400px;
  margin: 0 auto;
}
</style>
