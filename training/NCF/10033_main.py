import itertools

from GCN.training.NCF import model_utils


def main():
    use_implicit = False
    if use_implicit:
        model_name = "NCF"
    else:
        model_name = "NCF_use_only_explicit"
    num_factors = [32]
    batch_sizes = [1024, 2048]
    learning_rates = [0.001, 0.01]
    num_negs = [4]
    num_epochs = [100]

    available_gpu = ["0", "1"]
    visible_gpu = ",".join(available_gpu[0])
    for data_name in ["hetrec2011-lastfm-2k/"]:
        hyper_params = {
            "verbose": 10,
            "eval_top_k": 10,
            "lambda": 0.005,
            "data_name": data_name,
            "model_name": model_name,
            "use_implicit": use_implicit,
            "visible_gpu": visible_gpu
        }

        # init data
        m = model_utils.Utils(hyper_params, save_eval_result=True, save_model=True)
        for num_factor, batch_size, lr, num_neg, num_epoch in itertools.product(num_factors, batch_sizes,
                                                                                learning_rates, num_negs, num_epochs):
            hyper_params = {
                "num_factor": num_factor,
                "batch_size": batch_size,
                "lr": lr,
                "num_neg": num_neg,
                "num_epoch": num_epoch,
                "verbose": 10,
                "eval_top_k": 10,
                "lambda": 0.005,
                "data_name": data_name,
                "model_name": model_name,
                "use_implicit": use_implicit,
                "visible_gpu": visible_gpu
            }
            m.run(hyper_params, save_eval_result=True, save_model=True)


if __name__ == "__main__":
    main()
