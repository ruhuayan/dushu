function getTitle(vm) {
    const { title } = vm.$options;
    if (title) {
        return typeof title === "function" ? title.call(vm) : title;
    }
}
export default {
    created() {
        const title = getTitle(this);
        if (title && typeof document !== 'undefined') {
            document.title = title;
        }
    },
    watch: {
        $route() {
            const title = getTitle(this);
            if (title && typeof document !== 'undefined') {
                document.title = title;
            }
        },
    },
};
