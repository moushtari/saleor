import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    include: [__dirname + '*/tests/**/*.test.ts'],
    reporters: ['default', 'html'],
    outputFile: '*/tests/reports',
  },
})