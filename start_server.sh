#!/bin/bash

# Start local server for KOSAI website

cd "$(dirname "$0")/kosai-official-website"

echo "🚀 Starting local server..."
echo ""
echo "🌐 Your website will be available at:"
echo "   http://localhost:8000"
echo ""
echo "📁 Serving from: $(pwd)"
echo ""
echo "🛑 Press Ctrl+C to stop the server"
echo ""

python3 -m http.server 8000

