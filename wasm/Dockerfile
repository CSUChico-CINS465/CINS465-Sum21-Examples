FROM rust
RUN curl https://rustwasm.github.io/wasm-pack/installer/init.sh -sSf | sh
RUN cargo install cargo-generate
RUN mkdir /code
WORKDIR /code
