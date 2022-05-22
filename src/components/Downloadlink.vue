<template>
    <div class="downloaded_count">
        <div class="download_ebook_count">
            Ebook下载次数: 
            <span :class="{hasSeries: book.e_count === null}">
                {{ book.e_count ?? '无下载记录' }}
            </span>
            <a
                :href="`/ebooks/${book.title}/${book.title}.mobi`"
                target="_blank"
                @click="downloadEbook(book.id)"
                title="下载 ebook"
            >
                <svg>
                    <use xlink:href="#download" />
                </svg>
            </a>
        </div>
        <div class="download_pdf_count">
            PDF下载次数: 
            <span :class="{hasSeries: book.pdf_count === null}">
                {{ book.pdf_count ?? '无下载记录'  }}
            </span>
            <a
                :href="`/ebooks/${book.title}/${book.title}.pdf`"
                target="_blank"
                @click="downloadPdf(book.id)"
                title="下载 pdf"
            >
                <svg>
                    <use xlink:href="#download" />
                </svg>
            </a>
        </div>
    </div>
</template>
<script>
export default {
    name: "Downloadlink",
    props: {
        book: {
            type: Object,
            required: true,
        },
    },
    methods: {
        downloadEbook: function (bookId) {
            this.$store.dispatch("downloadEbook", bookId);
        },
        downloadPdf: function (bookId) {
            this.$store.dispatch("downloadPdf", bookId);
        },
    },
};
</script>
<style scoped>
span.hasSeries + a {
    display: none;
}
</style>