<template>
    <div>
        <p>{{ todo.title }}</p>
    </div>
</template>

<script>
export default {
    name: 'Todo',
    props: [
        "todo"
    ],
    methods: {
        markComplete() {
            this.todo.completed = !this.todo.completed;
        }
    }
}
</script>

<style scoped>
    .completed {
        text-decoration: line-through;
    }
</style>

