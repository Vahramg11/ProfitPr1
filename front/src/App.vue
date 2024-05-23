<template>
  <div id="app">
    <nav class="bg-gray-800 text-white">
      <div class="max-w-7xl mx-auto px-2 sm:px-6 lg:px-8 py-4 flex justify-between items-center">
        <div class="flex">
          <router-link to="/home" class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Home</router-link>
          <router-link to="/polls" class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-sm font-medium">All Polls</router-link>
          <router-link to="/addpoll" class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Add Poll</router-link>
        </div>
        <div class="flex">
          <router-link to="/signin" class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Sign In</router-link>
          <router-link to="/signup" class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Sign Up</router-link>
        </div>
      </div>
    </nav>

    <router-view/>
  </div>
</template>

<style scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
}

nav {
  background-color: #2c3e50;
}
</style>
